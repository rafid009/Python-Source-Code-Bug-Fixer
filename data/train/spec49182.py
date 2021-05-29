import numpy as np 

def function(x):

	v3 = x
	p1 = 7
	x = x
	paths = []
	try:
		if x > 2:
			p1 = p1*p1
			paths.append(1)
		else:
			x = 5+9
			x = 2/x
			paths.append(2)
		if p1 <= 0:
			x = v3*1
			x = 0+x
			paths.append(3)
		else:
			x = 9*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))