import numpy as np 

def function(x):

	a1 = 1
	u9 = 5
	paths = []
	try:
		if u9 <= 8:
			a1 = 4*0
			a1 = 6+0
			a1 = u9/3
			paths.append(1)
		else:
			a1 = u9+8
			x = x+3
			a1 = u9/3
			paths.append(2)
		if a1 <= 6:
			a1 = a1*0
			a1 = a1-5
			u9 = x+6
			paths.append(3)
		else:
			u9 = 4+u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		a1 = u9**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))