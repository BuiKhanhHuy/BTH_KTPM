CREATE TABLE [dbo].[BookAuthor] (
    [BookID]      INT  NOT NULL,
    [AuthorID]    INT  NOT NULL,
    [PublishDate] DATE NULL,
    CONSTRAINT [PK_BookAuthor] PRIMARY KEY CLUSTERED ([BookID] ASC, [AuthorID] ASC),
    CONSTRAINT [FK_BookAuthor_Author] FOREIGN KEY ([AuthorID]) REFERENCES [dbo].[Author] ([Id]),
    CONSTRAINT [FK_BookAuthor_Book] FOREIGN KEY ([BookID]) REFERENCES [dbo].[Book] ([BookID])
);

