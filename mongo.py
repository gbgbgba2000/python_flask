#載入pymongo 元件
import pymongo
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId #載入objectid
uri = "mongodb+srv://colin:colinkokoko688@mycluster.pwngzeb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.website #選擇操作 test資料庫 (Oracle DB NAME)
collcetion=db.users #操作 user 集合 (Oracle table)
#--------------------insert---------------------

#寫入一筆資料(Collection.insert_one=Oracle inser into table 一筆資料 JSON格式)
# collcetion.insert_one({"name":"蔡榮峯",
#                        "email":"ABCD@GMAIL.COM",
#                        "empid":"z1485",
#                        "level":"WITS"})
#寫入一筆資料並回傳id(Collection.insert_one=Oracle inser into table 一筆資料 JSON格式)
# result_data=collcetion.insert_one({"name":"王小花",
#                        "email":"ABCD123@GMAIL.COM",
#                        "empid":"Z1486",
#                        "level":"CO"})

#print("新增完畢"+" 資料ID : "+str(result_data.inserted_id))
#寫入多筆資料(Collection.insert_many=Oracle inser into table 多筆資料 JSON格式)
# result_data=collcetion.insert_many([{"name":"王小中",
#                        "email":"ABCDEF123@GMAIL.COM",
#                        "empid":"Z1488",
#                        "level":"WITS"},

#                        {"name":"王小虎",
#                        "email":"ABCD12345@GMAIL.COM",
#                        "empid":"Z1489",
#                        "level":"CO"}])
# print("新增完畢"+" 資料ID : "+str(result_data.inserted_ids))

#--------------------select---------------------
#取得collection 中第一筆資料
# data1=collcetion.find_one()
# print(data1)
# #取得collection 中指定的一筆資料
# data2=collcetion.find_one({"name":"王小明",
#                            "empid":"Z1489"})
# print(data2)
# #取得collection 中指定id的一筆資料 指定回傳王小花的資料，與empid
# data_id=collcetion.find_one(ObjectId("6576f7415be472ae3dd82d2a"))
# print(data_id)
# print("王小花的empid : "+data_id["empid"])
# #取得collection 中所有資料
# data_cursor=collcetion.find()
# for doc in data_cursor:
#  print("data_cursor : ", doc)
# #取得collection 中所有資料，但只找empid欄位的資料
# data_cursor=collcetion.find()
# for doc in data_cursor:
#  print("data_cursor : ", doc["empid"])
# #取得collection 中所有資料，條件為empid=z1485跟name=蔡榮峯的結果
# data_cursor2=collcetion.find_one({"$and":[{"empid":"z1485"},{"name":"蔡榮峯"}]})
# #for doc in data_cursor2:
# print("empid=Z1485跟name=蔡榮峯的結果 : ", data_cursor2)
#取得collection 中所有資料，之後做反排序
cursor=collcetion.find({
   "$or":[
          {"empid":"1485"},
          {"level":"WITS"}
        ]
},sort=[("empid",pymongo.DESCENDING)])
for doc in cursor:
 print( doc)


#---------------更新update------------------
#取得collection 中 更新一筆資料，王小花資料更新empid Z開頭改成U開頭
# data_update=collcetion.update_one({"empid":"Z1489"},
#                                   {"$set":{"empid":"U1489"}})
# print("符合篩選的文件數 :"+str(data_update.matched_count))
# print("實際更新的文件數 :"+str(data_update.modified_count))

#取得collection 中 更新一筆資料，王小花資料刪除content欄位
# data_un_set=collcetion.update_one({"empid":"Z1489"},
#                                   {"$unset":{"content":"ENGLISG"}})
# print("符合篩選的文件數 :"+str(data_un_set.matched_count))
# print("實際更新的文件數 :"+str(data_un_set.modified_count))
# #取得collection 中更新多筆資料 level=CO 的 email都改成@umail.com
# data_update2=collcetion.update_many({"level":"CO"},{"$set":{"level":"uco"}})
# print("update_many符合篩選的文件數 :"+str(data_update2.matched_count))
# print("update_many實際更新的文件數 :"+str(data_update2.modified_count))
#---------------更新delete------------------
#取得collection 中 刪除一筆資料，王小中資料刪除
# data_delete=collcetion.delete_one({"empid":"Z1488"})
# print("data_delete實際刪除的文件數 :"+str(data_delete.deleted_count))
#取得collection 中 刪除多筆level為uco的資料
# data_deletes=collcetion.delete_many({"level":"uco"})
# print("data_deletes實際刪除的文件數 :"+str(data_deletes.deleted_count))