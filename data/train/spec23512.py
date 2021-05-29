import numpy as np 

def function(x):

	f7 = 0
	v0 = x
	paths = []
	try:
		if v0 <= 8:
			x = x*2
			f7 = x/9
			v0 = v0+8
			paths.append(1)
		else:
			f7 = f7/1
			v0 = 9+v0
			f7 = 6+2
			paths.append(2)
		if f7 <= 4:
			f7 = 9+f7
			x = x*1
			v0 = 7*1
			paths.append(3)
		else:
			v0 = v0/9
			f7 = 6-f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))