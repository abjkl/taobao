#! usr/bin/python
#coding=utf-8

from database_setup import Base, Item, Sell_info, Shop,Brand
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
import numpy as np
import pandas as pd
from pandas import DataFrame

# Create session and connect to DB
engine = create_engine('sqlite:///item.db',connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


item_list =[{'item_url': 'http://item.taobao.com/item.htm?id=41437165101', 'nick': 'moco官方旗舰店', 'num_iid': 41437165101, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i4/581746910/TB17IeFdYsTMeJjy1zbXXchlVXa_!!0-item_pic.jpg', 'reserve_price': '2499.00', 'seller_id': 581746910, 'title': 'MO&amp;Co.摩安珂女装显瘦纯色拉链字母直筒立领长袖中长款羽绒服moco', 'user_type': 1, 'volume': 1, 'zk_final_price': '749.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523755099515', 'nick': 'moco官方旗舰店', 'num_iid': 523755099515, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i1/TB1uVk9KXXXXXb9XFXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '1199.00', 'seller_id': 581746910, 'title': 'MOCO秋冬女包边圆领短袖蕾丝刺绣图案T桖MA144SHT16 摩安珂', 'user_type': 1, 'volume': 0, 'zk_final_price': '359.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523377171039', 'nick': 'moco官方旗舰店', 'num_iid': 523377171039, 'pict_url': 'http://img4.tbcdn.cn/tfscom/i2/TB15B7uKXXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '1299.00', 'seller_id': 581746910, 'title': 'MOCO圆领长袖烫珠亚克力水钻花卉简约纯棉T恤MA144TST20 摩安珂', 'user_type': 1, 'volume': 7, 'zk_final_price': '389.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=522895215104', 'nick': 'moco官方旗舰店', 'num_iid': 522895215104, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i4/581746910/TB1o9scgyAKL1JjSZFoXXagCFXa_!!0-item_pic.jpg', 'reserve_price': '9999.00', 'seller_id': 581746910, 'title': 'MOCO秋冬秋女撞色狐狸毛皮草短款暗扣外套MA153PEE03 摩安珂', 'user_type': 1, 'volume': 0, 'zk_final_price': '5999.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=41247508931', 'nick': 'moco官方旗舰店', 'num_iid': 41247508931, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i1/TB1oqnFGXXXXXXSXVXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '1099.00', 'seller_id': 581746910, 'title': 'MOCO休闲裤女直筒显瘦中腰长裤格子文艺M143CAS32 摩安珂', 'user_type': 1, 'volume': 7, 'zk_final_price': '329.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=43436732308', 'nick': 'moco官方旗舰店', 'num_iid': 43436732308, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i4/TB1PD8THXXXXXcLXFXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '2699.00', 'seller_id': 581746910, 'title': 'MOCO摩安珂 呢大衣两件套中长款长袖翻领连帽MK144OVC01 摩安珂', 'user_type': 1, 'volume': 2, 'zk_final_price': '809.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=40565575944', 'nick': 'moco官方旗舰店', 'num_iid': 40565575944, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i4/TB1bivUGVXXXXX6XFXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '2199.00', 'seller_id': 581746910, 'title': 'MOCO摩安珂女装肌理感羽绒服简约圆领秋冬M143EIN19 摩安珂', 'user_type': 1, 'volume': 1, 'zk_final_price': '989.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=43943325217', 'nick': 'moco官方旗舰店', 'num_iid': 43943325217, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i3/581746910/TB1aSoygu7JL1JjSZFKXXc4KXXa_!!0-item_pic.jpg', 'reserve_price': '1599.00', 'seller_id': 581746910, 'title': 'MOCO阔腿武士裤七分宽松裙裤复古MA151CAS29 摩安珂', 'user_type': 1, 'volume': 7, 'zk_final_price': '479.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=524727199220', 'nick': 'moco官方旗舰店', 'num_iid': 524727199220, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i3/581746910/TB1bjhXX.6FK1Jjy0FlXXXntVXa_!!0-item_pic.jpg', 'reserve_price': '2099.00', 'seller_id': 581746910, 'title': 'MOCO羊毛欧根纱拼接纽扣短款针织开衫毛衣外套MA154JEY66 摩安珂', 'user_type': 1, 'volume': 3, 'zk_final_price': '879.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=44133313223', 'nick': 'moco官方旗舰店', 'num_iid': 44133313223, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i3/581746910/TB1QJNEa3MPMeJjy1XcXXXpppXa_!!0-item_pic.jpg', 'reserve_price': '1099.00', 'seller_id': 581746910, 'title': '摩安珂 夏季款圆领短袖条纹拼接女士连衣裙 欧美时尚连身裙 moco', 'user_type': 1, 'volume': 8, 'zk_final_price': '269.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523816984984', 'nick': 'moco官方旗舰店', 'num_iid': 523816984984, 'pict_url': 'http://img4.tbcdn.cn/tfscom/i3/TB1zC3dKXXXXXbmXVXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '3599.00', 'seller_id': 581746910, 'title': 'MOCO兔毛皮绵羊皮革拼接拉链门襟秋季长袖皮草MA144PEE04 摩安珂', 'user_type': 1, 'volume': 0, 'zk_final_price': '3599.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=528323891387', 'nick': 'moco官方旗舰店', 'num_iid': 528323891387, 'pict_url': 'http://img3.tbcdn.cn/tfscom/i4/581746910/TB1cZjZaqagSKJjy0FgXXcRqFXa_!!0-item_pic.jpg', 'reserve_price': '1199.00', 'seller_id': 581746910, 'title': 'MOCO宽松休闲直筒西装阔腿裤可调节九分背带裤MA161CAS34 摩安珂', 'user_type': 1, 'volume': 6, 'zk_final_price': '719.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523371721338', 'nick': 'moco官方旗舰店', 'num_iid': 523371721338, 'pict_url': 'http://img4.tbcdn.cn/tfscom/i2/TB1l4H3IVXXXXalXFXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '1099.00', 'seller_id': 581746910, 'title': 'MOCO秋装女短款落肩袖休闲黑白条纹毛衣MA144JEY58 摩安珂', 'user_type': 1, 'volume': 0, 'zk_final_price': '499.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=45013402764', 'nick': 'moco官方旗舰店', 'num_iid': 45013402764, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i4/581746910/TB1Rkcqb8cHL1JjSZFBXXaiGXXa_!!0-item_pic.jpg', 'reserve_price': '899.00', 'seller_id': 581746910, 'title': 'MO&amp;Co.背心女夏大码条纹字母无袖露腰时尚简约上衣MA152VET01moco', 'user_type': 1, 'volume': 0, 'zk_final_price': '479.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523279911407', 'nick': 'moco官方旗舰店', 'num_iid': 523279911407, 'pict_url': 'http://img4.tbcdn.cn/tfscom/i1/581746910/TB1Dfhua3sSMeJjSspdXXXZ4pXa_!!0-item_pic.jpg', 'reserve_price': '1099.00', 'seller_id': 581746910, 'title': 'MOCO秋冬高领镂空蕾丝T恤长袖打底衫上衣衬衫MA144SHT15 摩安珂', 'user_type': 1, 'volume': 10, 'zk_final_price': '329.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=38579124109', 'nick': 'moco官方旗舰店', 'num_iid': 38579124109, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i4/581746910/TB10.7kb7.HL1JjSZFlXXaiRFXa_!!0-item_pic.jpg', 'reserve_price': '699.00', 'seller_id': 581746910, 'title': 'MOCO摩安珂女装新款短裙欧美荷叶边纯色半身裙M142SKT219 摩安珂', 'user_type': 1, 'volume': 1, 'zk_final_price': '189.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=522088477960', 'nick': 'moco官方旗舰店', 'num_iid': 522088477960, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i4/581746910/TB1ARS2XekJL1JjSZFmXXcw0XXa_!!0-item_pic.jpg', 'reserve_price': '899.00', 'seller_id': 581746910, 'title': 'MOCO豹纹套头T恤女长袖圆领动物贴布绣MA153TST10 摩安珂', 'user_type': 1, 'volume': 0, 'zk_final_price': '539.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=42635033284', 'nick': 'moco官方旗舰店', 'num_iid': 42635033284, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i2/TB1zjCkGVXXXXbKXXXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '1599.00', 'seller_id': 581746910, 'title': 'MOCO摩安珂 衬衫长袖女印花荷叶边拼接欧美MA144SHT02 摩安珂', 'user_type': 1, 'volume': 2, 'zk_final_price': '479.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=41011418920', 'nick': 'moco官方旗舰店', 'num_iid': 41011418920, 'pict_url': 'http://img1.tbcdn.cn/tfscom/i2/581746910/TB1ZA9EXfBNTKJjy1zdXXaScpXa_!!0-item_pic.jpg', 'reserve_price': '1399.00', 'seller_id': 581746910, 'title': 'MOCO摩安珂女装短款开衫外套百搭长袖油印花M143COT66 摩安珂', 'user_type': 1, 'volume': 3, 'zk_final_price': '419.00'}, {'item_url': 'http://item.taobao.com/item.htm?id=523305109201', 'nick': 'moco官方旗舰店', 'num_iid': 523305109201, 'pict_url': 'http://img2.tbcdn.cn/tfscom/i1/TB1AUGKKXXXXXa0XVXXXXXXXXXX_!!0-item_pic.jpg', 'reserve_price': '2699.00', 'seller_id': 581746910, 'title': 'MOCO羽绒服女针织围巾领不规则短款磁铁吸扣MA144EIN15 摩安珂', 'user_type': 1, 'volume': 2, 'zk_final_price': '809.00'}]


# for i in item_list:
#
#     if len(session.query(Item).filter_by(tb_id=i['num_iid']).all()) == 0:
#         newitem = Item(title=i['title'],
#                        price=i['reserve_price'],
#                        pic=i['pict_url'],
#                        tb_id=i['num_iid'])
#         session.add(newitem)
#         session.commit()
#
#     if len(session.query(Sell_info).filter_by(tb_id=i['num_iid'],price=i['zk_final_price'],date=datetime.date.today()).all()) == 0:
#         newprice = Sell_info(tb_id=i['num_iid'],
#                              price=i['zk_final_price'],
#                              tb_sid=i['seller_id'])
#         session.add(newprice)
#         session.commit()
#
#     if len(session.query(Shop).filter_by(tb_sid=i['seller_id']).all())== 0:
#         newshop = Shop(tb_sid=i['seller_id'],
#                        name=i['nick'])
#         session.add(newshop)
#         session.commit()


# item1 = session.query(Item).filter_by(id=500).one()

# list = []
# for line in open('/Users/gaoxinyi/Desktop/list.txt'):
#     list.append(line)
#
# print(list)

list = ['moco官方旗舰店', '海尔官方旗舰店', '伊丽莎白雅顿海外旗舰店', '伊丽莎白雅顿官方旗舰店', '天猫国际官方直营',
        '小也官方旗舰店', 'chemistwarehouse海外旗舰', 'liking海外旗舰店', '当当网官方旗舰店', 'aldi海外旗舰店', 'neiwai内衣旗舰店', 'newlookmarket海外旗舰店', '欧缇丽官方旗舰店', '阿里健康海外旗舰店', 'paraseller海外旗舰店', 'farmacity海外旗舰店', 'snidel官方旗舰店', 'newlook官方旗舰店', '初语箱包旗舰店', '初语旗舰店', 'ajoysahu海外旗舰店', 'cpu旗舰', 'forever21官方旗舰店', 'pullandbear官方旗舰店', 'gap官方旗舰店', 'esprit官方旗舰店', '魅力惠海外旗舰店', '客邻尚品海外旗舰店', 'ugg官方旗舰店', 'ugg童鞋旗舰店', 'toms旗舰店', 'nativeshoes旗舰店', '银泰百货精品旗舰店', 'levis鞋类旗舰店', 'axonus海外专营店', 'oysho官方旗舰店', '速写官方旗舰店', '欧莱雅集团小美盒旗舰店', '玛依恋旗舰店', '彩依恋旗舰店', '杰杰丝旗舰店', '索莎娜旗舰店', 'eland官方旗舰店', '中农百粮食品专营店', 'crocs户外旗舰店', 'stellaluna旗舰店', 'teenieweenie官方旗舰店', 'skechers海外旗舰店', 'skechers运动旗舰店', 'skechers童鞋旗舰店', 'vans官方旗舰店', 'sneakerhead海外旗舰店', 'newbalance旗舰店', 'converse官方旗舰店', 'adidas官方旗舰店', 'lacoste官方旗舰店', 'tommyhilfiger官方旗舰店', 'clarks女鞋旗舰店', 'macys官方海外旗舰店', '江南布衣官方旗舰店', 'underarmour官方旗舰店', 'underarmour跑步旗舰店', 'thenorthface官方旗舰', 'columbia官方旗舰店', 'tiger虎牌官方旗舰店', 'onitsukatiger官方旗舰店', 'achette雅氏旗舰店', '狮王官方旗舰店', '雪肌精官方旗舰店', 'ora2皓乐齿旗舰店', 'harborhouse家居店', '关茶旗舰店', 'shiseido资生堂官方旗舰店', '雅诗兰黛官方旗舰店', '欧莱雅官方旗舰店', 'lamer海蓝之谜官方旗舰店', 'clinique倩碧官方旗舰店', 'lancome兰蔻官方旗舰店', '后官方旗舰店', 'biotherm碧欧泉官方旗舰店', '兰芝官方旗舰店', '茱莉蔻官方旗舰店', '法国娇韵诗官方旗舰店', '悦木之源官方旗舰店', 'hr赫莲娜官方旗舰店', '雅漾官方旗舰店', 'cozzolino海外旗舰店', '梦妆官方旗舰店', '露得清官方旗舰店', '万宁官方海外旗舰店', '佰草集官方旗舰店', '高丝官方旗舰店', '蜜丝佛陀官方旗舰店', 'dhc蝶翠诗官方旗舰店', '美宝莲旗舰店', '美即官方旗舰店', 'ninewest玖熙旗舰店', 'keds旗舰店', 'charleskeith旗舰店', 'samedelman旗舰店', 'naturalizer旗舰店', 'havaianas旗舰店', '乐高官方旗舰店', '雀巢官方旗舰店', '格兰仕官方旗舰店', 'twinings官方旗舰店', '北岛北方食品专营店', '好时巧克力旗舰店', '佳沃水果旗舰店', 'durex杜蕾斯官方旗舰店', '九阳官方旗舰店', '苏泊尔官方旗舰店', '飞利浦官方旗舰店', 'swisse官方海外旗舰店', '肌肤哲理官方旗舰店', '肌肤之钥官方旗舰店', 'evelom官方旗舰店', 'amazon官方旗舰店', 'dolcegusto官方旗舰店', '科沃斯旗舰店', '香港卓悦海外旗舰店', 'sparllo官方海外旗舰店', 'doshisha海外旗舰店', 'thermos膳魔师海外旗舰店', 'freepeople海外旗舰店', 'pola宝丽官方旗舰店', 'noevir诺薇雅旗舰店', '贝德玛旗舰店', 'reebonz海外旗舰店', 'furla官方旗舰店', '银泰意选海外旗舰店', 'forzieri海外旗舰店']

querys = ['MOCO','伊丽莎白雅顿','NEIWAI内外','欧缇丽','snidel','NEWLOOK','初语','AJOY SAHU','Forever21','PullAndBear',
         'Gap','ESPRIT','UGG','toms','nativeshoes','MAX MARA','Levi\'s','Oysho','速写男装','蕉下','欧莱雅','ELAND','Crocs','stellaluna',
         'Teenie Weenie','Skechers','Vans',"Jimmy Choo",'海尔','converse','lacoste','adidas','clarks','tommyhilfiger','安德玛',
          'thenorthface','江南布衣','columbia','tiger','onitsukatiger','achette','狮王','雪肌精','ora2','关茶','shiseido','雅诗兰黛','欧莱雅','lamer',
          'clinique','lancome','后','biotherm','兰芝','茱莉蔻','娇韵诗','悦木之源','hr赫莲娜','雅漾','梦妆','露得清','佰草集','高丝','蜜丝佛陀','dhc','美宝莲',
          '美即','ninewest','keds','charles&keith','samedelman','naturalizer','havaianas','乐高','雀巢','格兰仕','twinings','好时','杜蕾斯','九阳','肌肤之钥',
          'evelom','amazon','dolcegusto','科沃斯','thermos','freepeople','pola','noevir','furla','SK2','Givenchy','valentino','Theory','Bally','Armani',
          'Tom Ford','Gucci','Prada','YSL','Dior','OPENING CEREMONY']

brands = ['MOCO','伊丽莎白雅顿','NEIWAI内外','欧缇丽','snidel','NEWLOOK','初语','AJOY SAHU','Forever21','PullAndBear',
         'Gap','ESPRIT','UGG','toms','nativeshoes','MAX MARA','Levi\'s','Oysho','速写男装','蕉下','欧莱雅','Eland','Crocs','Stella Luna',
         'Teenie Weenie','Skechers','Vans',"Jimmy Choo",'海尔','匡威','Lacoste','阿迪达斯','Clarks','Tommy Hilfiger','安德玛',
          'thenorthface','江南布衣','Columbia','虎牌','鬼冢虎','雅氏','狮王','雪肌精','ora2','关茶','资生堂','雅诗兰黛','欧莱雅','La Mer',
          '倩碧','兰蔻','后','碧欧泉','兰芝','茱莉蔻','娇韵诗','悦木之源','hr赫莲娜','雅漾','梦妆','露得清','佰草集','高丝','蜜丝佛陀','DHC','美宝莲',
          '美即','玖熙','Keds','Charles&Keith','Sam Edelman','Naturalizer','havaianas','乐高','雀巢','格兰仕','川宁','好时','杜蕾斯','九阳','肌肤之钥',
          'EVE LOM','amazon','Dolcegusto','科沃斯','膳魔师','freepeople','pola','noevir','Furla','SK2','Givenchy','Valentino','Theory','Bally','Armani',
          'Tom Ford','Gucci','Prada','YSL','Dior','OPENING CEREMONY']

# for i in brands:
#     newbrand=Brand(name=i)
#     session.add(newbrand)
#     session.commit()

# all_id = session.query(Sell_info).with_entities(Sell_info.tb_id).all()
# shops = session.query(Shop).all()
# items = session.query(func.count(Sell_info.id)).scalar()
# mark = session.query(Item).filter(Item.title.like("%clinique%")).all()

# X = session.query(Sell_info.price,Sell_info.tb_sid,Item.tb_id,Item.price).join(Item,Item.tb_id == Sell_info.tb_id).all()
#
# Y = session.query(Sell_info.recom).all()
#
# print (type(Y[0]))

# for i in range (0,102):
#     print (i)
#     query = querys[i]
#
#     mark = session.query(Item).filter(Item.title.like("%"+query+"%")).all()
#     for x in mark:
#         x.brand = brands[i]
#         session.add(x)
#         session.commit()



df1 = pd.read_sql(session.query(Sell_info.price,Sell_info.tb_sid,Item.tb_id,Item.price,Sell_info.recom).join(Item,Item.tb_id == Sell_info.tb_id).statement,session.bind)
df1.rename(columns=('price': , 'dis': 'b', '$c': 'c', '$d': 'd', '$e': 'e'}, inplace=True)
# df1=df1.sample(frac=1.0)
# cut_idx=int(round(0.1*df1.shape[0]))
# df_test, df_train = df1.iloc[:cut_idx], df1.iloc[cut_idx:]
# X=df_test['price','tb_id','tb_sid','price']




