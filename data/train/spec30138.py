import numpy as np 

def function(x):

	l8 = x
	w5 = x
	paths = []
	try:
		if l8 <= 2:
			x = 3/l8
			paths.append(1)
		else:
			l8 = l8*0
			x = x/1
			x = x-l8
			paths.append(2)
		if w5 <= 4:
			w5 = l8*9
			w5 = w5-6
			paths.append(3)
		else:
			x = x-0
			l8 = l8+9
			w5 = w5/9
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))