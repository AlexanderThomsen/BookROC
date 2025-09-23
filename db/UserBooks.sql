CREATE TABLE UserBooks (
    UserBookID INT IDENTITY(1,1) PRIMARY KEY, 
    UserID INT NOT NULL,                       
    BookID INT NOT NULL,                       
    Status NVARCHAR(20) NOT NULL,             
    Rating TINYINT,                            
    CONSTRAINT FK_User FOREIGN KEY (UserID) REFERENCES Users(UserID),
    CONSTRAINT FK_Book FOREIGN KEY (BookID) REFERENCES Books(BookID),
    CONSTRAINT CHK_Status CHECK (Status IN ('read', 'wishes', 'favorite')),
    Created_At DATETIME2 DEFAULT GETDATE(),
    Updated_At DATETIME2 DEFAULT GETDATE()
);
