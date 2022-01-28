# defer

我们经常使用defer关键字来关闭资源，处理recover panic等。这里来详细研究一下defer的使用与原理。



### 使用场景

1. 关闭资源

   ```go
   func createPost(db *gorm.DB) error {
       tx := db.Begin()
       defer tx.Rollback()
       
       if err := tx.Create(&Post{Author: "Draveness"}).Error; err != nil {
           return err
       }
       
       return tx.Commit().Error
   }
   ```

2. 处理程序panic

   ```go
   func handle(){
   	defer func(){
   		if err := recover();err != nil{
   			fmt.Println("err:",err)
   		}
   	}()
   	fmt.Println(213214)
   }
   ```

   

### 使用方式

我们在使用defer是要注意两个方面：

1. defer的调用时机 && 多个defer之间的执行顺序
2. defer中传递参数时预结算，造成预期不符





### 发展历程

1. 堆上分配

   todo

2. 栈上分配

   todo

3. 开发编码

   todo