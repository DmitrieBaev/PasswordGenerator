class PasswordGenerator:
    """ Генератор пароля """
    
    def __init__( self, password_length: int, use_specials=False, specials_template=r'+-/*!()\'&[]${}#?;^=@<:%>"|_\.`,~' ):
        """
        Генератор пароля
        
        :param password_length: Длина пароля
        :type password_length: Integer
        :param only_nums: Использовать только числа
        :type only_nums: Boolean
        :param only_chars: Использовать только буквы
        :type only_chars: Boolean
        :param specials_template: Какие спец-символы можно использовать
        :type specials_template: String
        """
        self.password_length = password_length
        self.template = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQR'
        if use_specials: self.template += specials_template
    
    def generate( self, password_counts=1 ) -> list:
        """
        Генерация пароля
        
        :param password_counts: Количество генерируемых паролей
        :type password_counts: Integer
        :return: Пароли
        :rtype: Array
        """
        import random as rnd
        
        return [''.join(rnd.sample(self.template, self.password_length)) for _ in range(password_counts)]
    
    # Официальное строковое представление
    def __repr__( self ) -> str:
        return f'{self.__class__.__name__}' \
               f'(password_length=16, use_specials=True, ' \
               r'specials_template=\'+-/*!()\'&[]${}#?;^=@<:%>"|_\.`,~\')'
    
    # Неформальное строковое представление
    def __str__( self ) -> str: return self.__repr__( )


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1: print('help')
    if len(sys.argv) == 2: print(PasswordGenerator(int(sys.argv[1])).generate( ))
    if len(sys.argv) == 3: print(PasswordGenerator(int(sys.argv[1])).generate(int(sys.argv[2])))
    if len(sys.argv) >= 4: print('Coming soon...')
