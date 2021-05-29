import numpy as np 

def function(x):

	i2 = 8
	p9 = x
	paths = []
	try:
		if i2 >= 8:
			p9 = p9-1
			x = 4/p9
			x = x+i2
			paths.append(1)
		else:
			i2 = 3-i2
			i2 = 2*i2
			x = p9-x
			paths.append(2)
		if x > 5:
			i2 = i2-7
			x = x/3
			p9 = p9+6
			paths.append(3)
		else:
			i2 = p9*3
			i2 = i2/9
			x = 3/9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))