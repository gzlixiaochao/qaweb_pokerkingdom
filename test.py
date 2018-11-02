from app import sql_exe_search, sql1


sql1 = "select * from user_details_info t where t.nike_name= '李晓超004'"
print(sql_exe_search(sql1))