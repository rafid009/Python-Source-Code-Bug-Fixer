import numpy as np 

def function(x):

	u9 = x
	p5 = 9
	paths = []
	try:
		if p5 < 9:
			x = x*2
			paths.append(1)
		else:
			x = 0+x
			x = x+x
			paths.append(2)
		if p5 < 6:
			x = 1/5
			paths.append(3)
		else:
			u9 = u9*5
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))