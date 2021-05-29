import numpy as np 

def function(x):

	r7 = 7
	u6 = x
	paths = []
	try:
		if x <= 3:
			r7 = r7*9
			paths.append(1)
		else:
			u6 = u6-r7
			r7 = 2/3
			paths.append(2)
		if r7 < 0:
			u6 = r7+9
			u6 = u6*5
			paths.append(3)
		else:
			u6 = u6+u6
			x = x+6
			x = x*r7
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		r7 = u6**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))