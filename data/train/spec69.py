import numpy as np 

def function(x):

	a9 = x
	u5 = 1
	x = x
	paths = []
	try:
		if a9 > 7:
			u5 = 2+x
			a9 = 8+a9
			a9 = 4/9
			paths.append(1)
		else:
			u5 = 0*u5
			a9 = 9/a9
			x = 3*0
			paths.append(2)
		if u5 < 1:
			u5 = 8-4
			x = a9-x
			a9 = x/1
			paths.append(3)
		else:
			u5 = 0*u5
			x = x*0
			a9 = 4*a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		u5 = a9**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))