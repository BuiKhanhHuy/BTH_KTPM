CREATE TABLE [dbo].[Book] (
    [BookID]     INT           NOT NULL,
    [BookName]   NVARCHAR (50) NULL,
    [CategoryID] INT           NULL,
    CONSTRAINT [PK_Book] PRIMARY KEY CLUSTERED ([BookID] ASC),
    CONSTRAINT [FK_Book_Category] FOREIGN KEY ([CategoryID]) REFERENCES [dbo].[Category] ([CategoryID])
);

