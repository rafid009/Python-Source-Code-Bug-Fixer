import numpy as np 

def function(x):

	p6 = 5
	f3 = x
	x = x
	paths = []
	try:
		if p6 > 3:
			p6 = 4+p6
			paths.append(1)
		else:
			x = x+f3
			paths.append(2)
		if f3 > 6:
			f3 = 0+9
			x = x-9
			paths.append(3)
		else:
			x = 9*8
			p6 = 8-p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		f3 = p6**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))