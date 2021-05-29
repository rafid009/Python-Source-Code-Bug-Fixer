import numpy as np 

def function(x):

	p0 = 9
	f4 = x
	x = 1
	paths = []
	try:
		if f4 <= 4:
			f4 = f4+2
			x = 0*p0
			x = x+9
			paths.append(1)
		else:
			x = f4-x
			p0 = p0-6
			x = x+f4
			paths.append(2)
		if p0 > 5:
			x = p0-x
			paths.append(3)
		else:
			x = f4-x
			x = x*9
			x = x+f4
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