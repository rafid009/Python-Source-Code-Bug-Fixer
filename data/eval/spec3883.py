import numpy as np 

def function(x):

	j3 = 8
	p8 = x
	paths = []
	try:
		if p8 > 5:
			x = x+5
			j3 = 1/4
			j3 = j3/5
			paths.append(1)
		else:
			x = j3/x
			paths.append(2)
		if x > 3:
			p8 = j3/p8
			p8 = 0-p8
			paths.append(3)
		else:
			j3 = j3/9
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))