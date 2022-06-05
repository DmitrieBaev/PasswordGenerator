##
# Определяет исключение для пустоты
class EmptyArgument < StandardError; end

##
# Определяет исключение для неправильного формата
class UnexpectedArgument < StandardError; end

##
# Генерирует пароль заданной `длины`
# == Parameters:
# pwd_length::
#   [Integer] Длина генерируемого пароля.
#
# == Returns:
# [String] Cгенерированный пароль
#
# == Example:
#    generate(4) => `aSw2`
#    generate(10) => `-a1cW2~0x8`
#
# == Usage:
#    ruby main.rb [options]
def generate(pwd_length)
	# генерация пароля
	template = '+-/*!()&[]${}#?;^=@<:%>"|_\.`,~abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	pwd = ''
	pwd_length.times { pwd += template[rand( template.size )] }

	# returned value
	pwd
end

# Точка входа в программу
raise EmptyArgument if ARGV[0].instance_of? NilClass  # Проверка на пустоту
raise UnexpectedArgument if ARGV[0].to_i.zero?  # Проверка на int

generate ARGV[0].to_i
