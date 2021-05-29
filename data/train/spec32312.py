import numpy as np 

def function(x):

	d1 = x
	u1 = 9
	paths = []
	try:
		if d1 <= 6:
			x = x/5
			x = 2/6
			paths.append(1)
		else:
			u1 = u1/x
			u1 = 9-x
			paths.append(2)
		if u1 >= 5:
			d1 = d1+x
			paths.append(3)
		else:
			d1 = d1*9
			u1 = u1*0
			x = 4*8
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))