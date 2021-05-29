import numpy as np 

def function(x):

	q7 = 5
	v3 = x
	x = 1
	paths = []
	try:
		if v3 <= 4:
			q7 = v3+1
			paths.append(1)
		else:
			q7 = v3*v3
			x = x*x
			q7 = q7/x
			paths.append(2)
		if x > 5:
			x = x+x
			v3 = v3+0
			paths.append(3)
		else:
			v3 = v3-9
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))