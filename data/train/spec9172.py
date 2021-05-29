import numpy as np 

def function(x):

	p9 = x
	k6 = 8
	paths = []
	try:
		if p9 < 5:
			x = x+7
			p9 = p9*6
			paths.append(1)
		else:
			x = k6*x
			k6 = 1*k6
			paths.append(2)
		if x > 0:
			p9 = x*1
			k6 = 5/k6
			p9 = x+2
			paths.append(3)
		else:
			p9 = p9*5
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		k6 = p9**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))