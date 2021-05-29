import numpy as np 

def function(x):

	p9 = 5
	d9 = x
	paths = []
	try:
		if d9 <= 9:
			d9 = d9*0
			d9 = d9+p9
			d9 = d9-5
			paths.append(1)
		else:
			p9 = d9/d9
			paths.append(2)
		if d9 > 4:
			p9 = 1-5
			x = x/2
			paths.append(3)
		else:
			p9 = p9-0
			p9 = p9+d9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))