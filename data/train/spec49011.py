import numpy as np 

def function(x):

	p9 = 7
	i1 = x
	paths = []
	try:
		if x < 5:
			p9 = 4/i1
			i1 = 9/p9
			i1 = i1/4
			paths.append(1)
		else:
			i1 = 7-i1
			p9 = 9/p9
			paths.append(2)
		if x >= 0:
			x = x*2
			paths.append(3)
		else:
			i1 = i1/i1
			p9 = 4*1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		p9 = i1**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))