import numpy as np 

def function(x):

	p9 = x
	u6 = 3
	paths = []
	try:
		if p9 < 7:
			p9 = p9+1
			u6 = u6/9
			paths.append(1)
		else:
			u6 = 3/8
			u6 = 6+p9
			paths.append(2)
		if p9 >= 1:
			p9 = p9+2
			p9 = p9+u6
			u6 = u6*5
			paths.append(3)
		else:
			u6 = u6+9
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