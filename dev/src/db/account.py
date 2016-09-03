from config import *


class account(db_check):
	
	table_name="table_account_bank"
	table_Strutkur={'status': 'integer', 'amount': 'double precision', 'user_id': 'bigint', 'row': 'bigint'}
        
            
	def add(self, user_id=None, amount=None, status=None):
		
		return DB.insert(self.table_name, user_id=user_id, amount=amount, status=status)


	def set(self, user_id=None, amount=None, status=None, operation=""):

		where=""
		where=db.condition_and(where, "user_id", user_id)
			
		ret = DB.update1(self.table_name, where, operation, amount=amount, status=status)
		if not ret:
			ret=self.add(user_id, amount, status)
		return ret


	def get(self, user_id=None, amount=None, status=None, row=None):
		
		return DB.select1(self.table_name)
  
