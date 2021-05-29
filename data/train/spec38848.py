import numpy as np 

def function(x):

	j2 = x
	p9 = 0
	paths = []
	try:
		if p9 <= 9:
			p9 = 9+p9
			paths.append(1)
		else:
			j2 = j2*9
			x = j2/x
			j2 = p9+7
			paths.append(2)
		if j2 > 3:
			j2 = 0/p9
			paths.append(3)
		else:
			p9 = p9/j2
			j2 = 0+p9
			x = x*6
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		j2 = p9**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))