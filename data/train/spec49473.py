import numpy as np 

def function(x):

	p9 = x
	j8 = 1
	paths = []
	try:
		if p9 >= 4:
			p9 = p9/1
			j8 = j8+8
			j8 = 6+j8
			paths.append(1)
		else:
			p9 = x-x
			x = 4+0
			p9 = x-8
			paths.append(2)
		if p9 <= 3:
			x = x/1
			x = p9+4
			paths.append(3)
		else:
			p9 = p9/x
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