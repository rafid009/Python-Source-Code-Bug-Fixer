import numpy as np 

def function(x):

	v6 = x
	r4 = x
	paths = []
	try:
		if v6 <= 3:
			x = 3/x
			v6 = r4/3
			paths.append(1)
		else:
			v6 = x/v6
			x = x*4
			paths.append(2)
		if r4 >= 7:
			v6 = r4*0
			x = x/2
			r4 = 6-x
			paths.append(3)
		else:
			x = r4-9
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))