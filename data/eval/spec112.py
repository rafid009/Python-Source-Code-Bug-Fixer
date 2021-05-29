import numpy as np 

def function(x):

	p4 = 2
	i6 = x
	x = 7
	paths = []
	try:
		if i6 > 8:
			i6 = i6-7
			i6 = 6-i6
			i6 = i6-p4
			paths.append(1)
		else:
			i6 = x/i6
			x = x*2
			x = 6+x
			paths.append(2)
		if p4 < 5:
			x = x*0
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))