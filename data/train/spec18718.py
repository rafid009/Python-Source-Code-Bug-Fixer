import numpy as np 

def function(x):

	z9 = x
	q3 = 0
	paths = []
	try:
		if q3 >= 5:
			q3 = q3/5
			z9 = z9-0
			x = 4/9
			paths.append(1)
		else:
			q3 = 8*7
			z9 = 5-z9
			x = x/q3
			paths.append(2)
		if x <= 0:
			q3 = q3+q3
			x = x*0
			z9 = z9-5
			paths.append(3)
		else:
			x = x*x
			x = x+x
			x = x-7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		q3 = z9**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))