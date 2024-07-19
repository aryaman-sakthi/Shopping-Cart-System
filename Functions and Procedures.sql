use MiniProject;

drop procedure Add_to_Cart;
drop trigger Restock;
drop procedure generate_bill;
drop procedure item_details;


delimiter //
create procedure AddtoCart(
IN Order_No varchar(4),IN ItemID numeric(4), IN Quantity int)
Begin 
	declare Item_Price numeric(10,2) default 0;
    declare Unit_Price numeric(8,2) default 0;
    
    select price into Unit_Price from Items where I_ID=ItemID;
    
    set Item_Price = Unit_Price * Quantity;
    
    select I_ID,Name,Unit_Price,Item_Price from Items where I_ID=ItemID;
    
    update Inventory set Inventory.Quantity = Inventory.Quantity - Quantity
    where I_ID=ItemID;
    
    insert into Cart values(Order_No,ItemID,Quantity,Item_Price);
    
END//


delimiter //
create trigger Restock before update on Inventory 
for each row 
begin 
	if NEW.Quantity < 100 then 
    set NEW.Quantity = NEW.Quantity + 100;
End If;
END //



delimiter //
create Procedure Generate_Bill (
IN Billno varchar(4), OrderNo varchar(4))
Begin
	declare Customer numeric(3);
    declare Total_price int default 0;
    
    select C_ID into Customer from Orders
    where O_ID = OrderNo;
    
    select sum(Item_price) into Total_price from cart 
    group by order_No
    having Order_no = OrderNo;
    
    insert into Bill values (Billno,Customer,Total_price,curdate());
    select * from Bill where B_ID = Billno;
    
END //



delimiter //
create procedure item_details(
IN ItemID numeric(4))
Begin
	select * from items natural join manufacture
    where I_ID = ItemID;
END // 


    
    
	
	