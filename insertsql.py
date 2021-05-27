

# dealers = [
    # ['Marko Miskovic','Serbia'],
    # ['Darko Obradovic','France'],
    # ['Dragana Vukovic','Italy'],
    # ['Jelisaveta Lazovic','Australia']
# ]
# for dealer in dealers:
    # dealer_name = dealer[0]
    # country_id = dealer[1]
    
    # print(country_id)
    
    # country_name = dealer[1]
    # sql = """select country_id
    # from country
    # where country_name = '%s'
    # """ % (country_name,)
    # cur.execute(sql)
    # country_id = cur.fetchone()[0]
    
    # sql1 = """insert into dealers (dealer_name,country_id) values('%s',%s)""" %(dealer_name,country_id,)
    # cur.execute(sql1)
# db.commit()

# db.close()





contracts = [
        ['Nikola','2021-1-2','2022-1-2','asd345'],
        ['Milos','2019-2-3','2021-1-1','asdf456'],
        ['Petar','2020-4-5','2023-3-5','asght54']   
    ]
    

for contract in contracts:
    user_id = contract[0]
    valid_from = contract[1]
    valid_to = contract[2]
    contruct_number = contract[3]
    
    firstname = contract[0]
    
    sql = """select user_id
    from users
    where firstname = '%s'
    """ % (firstname)
    
    cur.execute(sql)
    user_id = cur.fetchone()[0]
    print(user_id)
    sql1 = """insert into contracts (user_id,valid_from,valid_to,contruct_number) values (%s,'%s','%s','%s')""" % (user_id,valid_from,valid_to,contruct_number,)
    cur.execute(sql1)
    
db.commit()
db.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
