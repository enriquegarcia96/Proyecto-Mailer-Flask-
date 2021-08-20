#instrucciones que se ejecutan cuando inicializo la base de datos
instructions = [
    'DROP TABLE IF EXISTS email',
    """
        CREATE TABLE email(
            id INT PRIMARY KEY AUTO_INCREMENT,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """
]