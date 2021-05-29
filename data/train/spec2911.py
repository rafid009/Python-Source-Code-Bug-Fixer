import numpy as np 

def function(x):

	v5 = x
	p9 = 6
	paths = []
	try:
		if p9 >= 5:
			x = x-x
			p9 = p9+2
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if p9 <= 6:
			v5 = 9/v5
			x = x*0
			paths.append(3)
		else:
			p9 = p9-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))