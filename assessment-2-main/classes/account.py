class Account:
    def __init__(self,level,restriction):
        self.amount=self.amount_Setter(level)
        self.restriction=self.restriction_Setter(restriction)

    def amount_Setter(self,level):
        if level=="s":
            return 1
        else:
            return 3
    def restriction_Setter(self,restriction):
        if restriction=="f":
            return "R"
        else:
            return None


# "sx" = standard account: max 1 rental out at a time
# "px" = premium account: max 3 rentals out at a time
# "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
# "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies
                    