import numpy as np 

def function(x):

	u5 = 7
	r8 = x
	paths = []
	try:
		if x > 8:
			x = 3*x
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if u5 >= 5:
			u5 = 2+u5
			u5 = x*0
			paths.append(3)
		else:
			u5 = r8*u5
			u5 = u5/2
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))