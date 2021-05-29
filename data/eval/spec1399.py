import numpy as np 

def function(x):

	b2 = 5
	f6 = x
	paths = []
	try:
		if b2 > 5:
			b2 = b2-b2
			b2 = x/b2
			b2 = 8+b2
			paths.append(1)
		else:
			b2 = 7+x
			b2 = x+7
			b2 = b2+b2
			paths.append(2)
		if f6 <= 7:
			b2 = b2/x
			paths.append(3)
		else:
			b2 = 8-b2
			f6 = 2/9
			f6 = 3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))