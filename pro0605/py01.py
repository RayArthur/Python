一、標準：ANSI-SQL (被大家所參考)
- Microsoft：Transact-SQL 
- SQLite: 沒有交易，他是很低階的資料庫
- 閃退裝況：
	- 變數會消失
	- 暫存表還會存留
- try-catch:
	- 指令錯：有錯誤，就全部失敗
	- 資料錯：有錯誤，就部份失敗。其他成功的會留存。
-- START 建立練習環境範例 ---------------------------
操作教務系統
use [教務系統]
-- 移除
drop table if exists t2
drop table if exists t1
drop table if exists t3
go
建立產品資料表
-- 產品資料表
create table t3	--< 產品資料表
( 
	產品編號 int primary key,
	產品名稱 varchar(10),
	庫存量 int)
go

insert into t3 values (1, '帽子', 10)
insert into t3 values (2, 'T恤', 10)
insert into t3 values (3, '褲子', 5)
go
建立訂單資料表
-- 訂單資料表
create table t1
(
	訂單編號 int primary key,
	訂單日期	date
)
go

insert into dbo.t1 values (1, '2020-06-01')
insert into dbo.t1 values (2, '2020-06-15')
go
建立_訂單明細表
-- 訂單明細資料表
create table t2
(
	訂單編號 int references dbo.t1,
	品項序號	int primary key(訂單編號, 品項序號),
	產品編號	int constraint fk_t2_產品編號 references dbo.t3,
	數量		int
)
go

insert into t2 values (1, 1, 1, 2)
insert into t2 values (1, 2, 2, 2)
insert into t2 values (1, 3, 3, 1)
insert into t2 values (2, 1, 2, 5)
go
-- END 建立練習環境範例 ----------------------------
二、簡單範例1：指令錯誤的try-catch
-- 簡單案例1
/*
 假設有一位員工進入訂單系統，根據客戶要求新增訂單：
 1) 新訂單訂購了尚未登錄的新產品編號4

*/
--begin transaction  --若失敗，則整筆不被記錄

declare @orderid int = 3		--< 訂單編號
declare @date date = GETDATE()	--< 訂單日期
declare @productno int = 4		--< 產品編號
declare @var int = 1			--<	客戶的訂購數量

-- 停用外部索引鍵(才能新增新的4號產品進入 產品資料表)
alter table t2 nocheck constraint [FK_t2_產品編號]

-- 新增訂單
insert into dbo.t1 ([訂單編號], [訂單日期])
values (@orderid, @date)

-- 新增訂單明細
insert into dbo.t2 ([訂單編號], [品項序號], [產品編號], [數量])
values (@orderid, 1, @productno, @var)

/*
	-- 另開查詢編輯器執行新產品
	insert into dbo.t3 values (4, '鞋子', 3)
*/

---二擇一
-- 啟用外部索引鍵，不檢查現存的資料
alter table t2 with nocheck check constraint [FK_t2_產品編號]
-- 啟用外部索引鍵，檢查現存的資料 (會導致失敗，因為產品編號裡面沒有4號)
--alter table t2 with check check constraint [FK_t2_產品編號]

-- 查詢該訂單
select t1.*, t2.品項序號, t3.產品名稱, t2.數量
from t1
	inner join t2 on t1.訂單編號 = t2.訂單編號
	left outer join t3 on t2.產品編號 = t3.產品編號
where t1.訂單編號 = @orderid

-- 復原
delete from dbo.t2 where t2.訂單編號 > 2
delete from dbo.t1 where t1.訂單編號 > 2
delete from dbo.t3 where t3.產品編號 = 4
go


三、資料錯誤的try-catch
在資料來源錯誤的情況下
	1. 沒有try-catch:
	   會新增3筆(1, 2, 4)
	2. 有try-catch:
	   有問題就跳出區塊
	3. 有begin transaction:
	   要馬全部完成、要馬步完成

-- 簡單案例2
--批次失敗的結果
drop table if exists #temp
create table #temp
( id int primary key,
  name varchar (2))
go

-- 假設以下是連續的大量資料匯入批次作業
--begin transaction
	begin try
		insert into #temp values (1, 'a')
		insert into #temp values (2, 'aa')
		insert into #temp values (3, 'aaa')  --即將發生問題的來源
		insert into #temp values (4, 'a')
		--commit transaction
	end try
	begin catch
                --rollback transaction
	end catch
go

select * from #temp
go

--commit tran

select * from #temp
go
--rollback

沒有try-catch:
	- 錯誤的不執行，其他成功
insert into #temp values (1, 'a')
insert into #temp values (2, 'aa')
insert into #temp values (3, 'aaa')  --即將發生問題的來源
insert into #temp values (4, 'a')


有try-catch:
	- 一有錯誤，就跳出區塊
	- 所以執行過的留存，沒被執行的就沒了
begin try
	insert into #temp values (1, 'a')
	insert into #temp values (2, 'aa')
	insert into #temp values (3, 'aaa')  --即將發生問題的來源
	insert into #temp values (4, 'a')
end try
begin catch

end catch


有begin trans  --測試開始
	- commit trans  --成功就存入
	- rollback trans --失敗就回朔
	- 全有全無策略
begin transaction
	begin try
		insert into #temp values (1, 'a')
		insert into #temp values (2, 'aa')
		insert into #temp values (3, 'aaa')  --即將發生問題的來源
		insert into #temp values (4, 'a')
		commit transaction
	end try
	begin catch
                rollback transaction
	end catch
空的
四、模擬熱區1
- 很多人同時讀取同一個資料表，那系統承受的壓力表現如何？
- 操作cmd多開視窗
	- 
	- 
	- 
	- 
	- 
20200706-Emp1.sql
set nocount on
use [教務系統]
begin transaction
--select * from t2 where [訂單編號] = 1
begin try
	update t2 set [數量] = 3 where [訂單編號] = 1 and [產品編號] = 1
	commit transaction
end try
begin catch
	rollback transaction
end catch
--select * from t2 where [訂單編號] = 1
set nocount off
20200706-Emp2.sql
set nocount on
use [教務系統]
begin transaction
--select * from t2 where [訂單編號] = 2
begin try
	update t2 set [數量] = 6 where [訂單編號] = 2 and [產品編號] = 2
	commit transaction
end try
begin catch
	rollback transaction
end catch
--select * from t2 where [訂單編號] = 2
set nocount off
p1.cmd
:begin
sqlcmd -i 20200706-Emp1.sql
sqlcmd -i 20200706-Emp2.sql
goto :begin
p2.cmd
:begin
sqlcmd -i 20200706-Emp2.sql
sqlcmd -i 20200706-Emp1.sql
goto :begin
五、模擬熱區2
- 更複雜點的檔案
- 
- 
- 
- 
- 
-- 簡單案例3
/*
 假設有兩位員工進入訂單系統，根據客戶要求修改訂單：
 1) 訂單編號1的產品編號1要修改訂購數量為3
 2) 訂單編號2的產品編號2要修改訂購數量為6
*/
-- 員工1
use [教務系統]
select * from t2 where [訂單編號] = 1
select getdate()
update t2 set [數量] = 3 where [訂單編號] = 1 and [產品編號] = 1
select getdate()
select * from t2 where [訂單編號] = 1

-- 員工2
use [教務系統]
select * from t2 where [訂單編號] = 2
update t2 set [數量] = 6 where [訂單編號] = 2 and [產品編號] = 2
select * from t2 where [訂單編號] = 2
-- 若以上的訂單處理啟用了明確的交易控制
--記錄更新時間
drop table if exists timelog
create table timelog
( Emp char(4),
  [before] datetime,
  [after] datetime )
go
20200706-Emp1.sql
-- 員工1：20200706-Emp1.sql
set nocount on
use [教務系統]
begin transaction
declare @before datetime
declare @after datetime
--select * from t2 where [訂單編號] = 1
--begin try
	set @before = getdate()
	update t2 set [數量] = 3 where [訂單編號] = 1 and [產品編號] = 1
	commit transaction
	set @after = getdate()
	insert into timelog values ('Emp1', @before, @after)
--end try
--begin catch
--	rollback transaction
--end catch
--select * from t2 where [訂單編號] = 1
set nocount off
go
20200706-Emp2.sql
-- 員工2：20200706-Emp2.sql
set nocount on
use [教務系統]
begin transaction
declare @before datetime
declare @after datetime
--select * from t2 where [訂單編號] = 2
--begin try
	set @before = getdate()
	update t2 set [數量] = 6 where [訂單編號] = 2 and [產品編號] = 2
	commit transaction
	set @after = getdate()
	insert into timelog values ('Emp2', @before, @after)
--end try
--begin catch
--	rollback transaction
--end catch
--select * from t2 where [訂單編號] = 2
set nocount off
go

-- 復原
update t2 set [數量] = 2 where [訂單編號] = 1 and [產品編號] = 1
update t2 set [數量] = 5 where [訂單編號] = 2 and [產品編號] = 2
go
p1.cmd
@echo off
:begin
sqlcmd -i 20200706-Emp1.sql
sqlcmd -i 20200706-Emp2.sql
goto :begin
p2.cmd
@echo off
:begin
sqlcmd -i 20200706-Emp2.sql
sqlcmd -i 20200706-Emp1.sql
goto :begin
六、實價登入
- csv -> python -> SQL
- 可直接讀取csv作分析的軟體：
	- Tableau_要錢
	- Power BI_不用錢
		- 從SQL讀出來
- git範本
先在SQL建立表格
/* 登記日期自 109年5月11 至 109年5月20日之買賣案件
 a_lvr_land_a_park.csv
*/
drop table if exists demo_park
create table demo_park
(
	SerialNumber varchar(20),
	BerthCategory nvarchar(10),
	BerthPrice	decimal(9,0),
	BerthAreaSquareMeter decimal(6, 2)
)
利用VSCode，製作出可連接至DB的字串
	- 相對路徑是"/"
	- 或利用 r" "
import pyodbc
import pandas as pd
df = pd.read_csv(r"C:\MSSQL\0706\lvr_landcsv\a_lvr_land_a_park.csv")
#df1 = pd.read_csv('C:/MSSQL/0706/lvr_landcsv/a_lvr_land_a.csv')

for index,  row in df.iterrows():
    sql_text = "insert into demo_part values('{}', '{}', {}, {})".format( row['編號'], row['車位類別'], row['車位價格'], row['車位面積平方公尺'])
    #print(row['編號'], row['車位類別'], row['車位價格'], row['車位面積平方公尺'])
    print(sql_text)
#-------




