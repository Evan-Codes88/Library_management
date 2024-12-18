from marshmallow import fields, ValidationError


from init import db, ma

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key = True)
    borrow_date = db.Column(db.Date, nullable = False)
    return_date = db.Column(db.Date, nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable = False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.id") , nullable = False)

    book = db.relationship("Book", back_populates = "loans")
    member = db.relationship("Member", back_populates = "loans")
   
    __table_args__ = (db.UniqueConstraint('book_id', 'member_id', name='uni_book_member'),)

class LoanSchema(ma.Schema):
    borrow_date = fields.Date(required=True)
    return_date = fields.Date(required=True)
    member_name = fields.Method("get_member_name")

    def validate_dates(self, data, **kwargs):
        """
        Validates the relationship between borrow_date and return_date.
        """
        borrow_date = data.get("borrow_date")
        return_date = data.get("return_date")

        if borrow_date and return_date:
            if return_date < borrow_date:
                raise ValidationError(
                    {"return_date": "Return date must be on or after the borrow date."}
                )

    def get_member_name(self, obj):
        return obj.member.name if obj.member else None

    class Meta:
        fields = ("id", "borrow_date", "return_date", "book_id", "member_id", "member_name")

loan_schema = LoanSchema()
loans_schema = LoanSchema(many = True)