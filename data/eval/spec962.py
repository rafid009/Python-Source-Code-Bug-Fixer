import numpy as np 

def function(x):

	f7 = 6
	p8 = x
	paths = []
	try:
		if p8 <= 0:
			f7 = f7+4
			f7 = 0/f7
			paths.append(1)
		else:
			x = 8+4
			f7 = f7*2
			paths.append(2)
		if f7 <= 1:
			x = x/8
			paths.append(3)
		else:
			f7 = f7+6
			x = x+2
			x = x/9
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))