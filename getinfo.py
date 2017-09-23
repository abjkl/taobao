import top.api
import json
from database_setup import Base, Item, Sell_info, Shop
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///item.db',connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


req=top.api.TbkItemGetRequest('gw.api.taobao.com',80)
req.set_app_info(top.appinfo('24628068', '9edd18df9631d0186511698f88e11c5e'))
req.fields="num_iid,title,pict_url,reserve_price,zk_final_price,user_type,item_url,seller_id,volume,nick"



def itemquery(query):
    req.q=query
    req.is_tmall = "true"
    result_num = req.getResponse()['tbk_item_get_response']['total_results']
    page = result_num // 100 + 1
    print (result_num)
    print (page)
    print (query)



    for i in (1,page):
        print (i)
        req.q = query
        req.sort = "tk_rate_des"
        req.is_tmall = "true"
        req.page_size = 100
        req.page_no=i
        resp = req.getResponse()
        result_list = (resp['tbk_item_get_response']['results']['n_tbk_item'])
        filldata(result_list)


def filldata(item_list):
    for i in item_list:
        if len(session.query(Shop).filter_by(tb_sid=i['seller_id']).all()) != 0:
            if len(session.query(Item).filter_by(tb_id=i['num_iid']).all()) == 0:
                newitem = Item(title=i['title'],
                               price=i['reserve_price'],
                               pic=i['pict_url'],
                               tb_id=i['num_iid'])
                session.add(newitem)
                session.commit()

            if len(session.query(Sell_info).filter_by(tb_id=i['num_iid'],price=i['zk_final_price'],date=datetime.date.today()).all()) == 0:
                newprice = Sell_info(tb_id=i['num_iid'],
                                     price=i['zk_final_price'],
                                     tb_sid=i['seller_id'])
                session.add(newprice)
                session.commit()


querys = ['MOCO','GU','魅力惠','伊丽莎白雅顿','ALDI','NEIWAI内外','欧缇丽','snidel','NEWLOOK','初语','AJOY SAHU','C.P.U.','Forever21','PullAndBear',
         'Gap','ESPRIT','UGG','toms 鞋','nativeshoes','MAX MARA','Levi\'s 鞋','Oysho','速写男装','蕉下','欧莱雅集团小美盒','ELAND','Crocs','stellaluna',
         'Teenie Weenie','Skechers','Vans',"Jimmy Choo",'海尔','skechers','converse','lacoste','adidas','clarks','tommyhilfiger','安德玛',
          'thenorthface','江南布衣','columbia','tiger','onitsukatiger','achette','狮王','雪肌精','ora2','关茶','shiseido','雅诗兰黛','欧莱雅','lamer',
          'clinique','lancome','后','biotherm','兰芝','茱莉蔻','娇韵诗','悦木之源','hr赫莲娜','雅漾','梦妆','露得清','佰草集','高丝','蜜丝佛陀','dhc','美宝莲',
          '美即','ninewest','keds','charles&keith','samedelman','naturalizer','havaianas','乐高','雀巢','格兰仕','twinings','好时','杜蕾斯','九阳','肌肤之钥',
          'evelom','amazon','dolcegusto','科沃斯','thermos','freepeople','pola','noevir','furla','SK2','Givenchy','valentino','Theory','Bally','Armani',
          'Tom Ford','Gucci','Prada','YSL','Dior','OPENING CEREMONY']

print (querys.index('charles&keith'))


for i in range(querys.index('havaianas'),len(querys)):
    itemquery(querys[i])