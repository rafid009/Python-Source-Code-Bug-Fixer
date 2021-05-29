import numpy as np 

def function(x):

	u5 = x
	f2 = 2
	paths = []
	try:
		if x < 7:
			f2 = f2+u5
			u5 = 2/2
			x = u5/x
			paths.append(1)
		else:
			u5 = 5/u5
			u5 = 0*0
			f2 = 1+f2
			paths.append(2)
		if u5 > 9:
			f2 = 5+u5
			u5 = u5+f2
			paths.append(3)
		else:
			x = x*3
			u5 = 2/1
			u5 = x*5
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