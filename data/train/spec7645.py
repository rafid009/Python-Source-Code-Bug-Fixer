import numpy as np 

def function(x):

	p9 = 1
	d6 = x
	paths = []
	try:
		if x >= 7:
			x = 8+p9
			paths.append(1)
		else:
			p9 = 3+p9
			p9 = 9+x
			p9 = 2-p9
			paths.append(2)
		if x > 9:
			x = 4/9
			d6 = 4*1
			x = 3*6
			paths.append(3)
		else:
			p9 = p9*8
			p9 = 6-7
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		d6 = p9**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))