import numpy as np 

def function(x):

	d6 = 9
	p9 = 7
	paths = []
	try:
		if d6 > 6:
			p9 = 7/5
			d6 = 6/x
			x = d6*p9
			paths.append(1)
		else:
			x = 3+7
			x = 8-p9
			paths.append(2)
		if p9 >= 6:
			x = 8-d6
			x = x*0
			p9 = 2/p9
			paths.append(3)
		else:
			x = 5*3
			x = x+2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))