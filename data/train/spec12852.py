import numpy as np 

def function(x):

	f4 = x
	p7 = 1
	paths = []
	try:
		if x <= 0:
			p7 = p7/f4
			p7 = 2+p7
			x = 7/x
			paths.append(1)
		else:
			f4 = f4-8
			f4 = 4+f4
			paths.append(2)
		if f4 <= 7:
			f4 = f4+1
			paths.append(3)
		else:
			x = x+7
			x = 8*x
			p7 = 3/p7
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))