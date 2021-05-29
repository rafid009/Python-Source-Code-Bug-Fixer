import numpy as np 

def function(x):

	i5 = 8
	z3 = 0
	paths = []
	try:
		if i5 <= 8:
			i5 = 5/6
			i5 = i5-x
			i5 = x*5
			paths.append(1)
		else:
			x = 7/9
			i5 = i5+0
			paths.append(2)
		if x >= 3:
			i5 = i5-4
			z3 = z3-2
			x = 4*0
			paths.append(3)
		else:
			i5 = 6+x
			x = x+1
			z3 = z3+z3
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))