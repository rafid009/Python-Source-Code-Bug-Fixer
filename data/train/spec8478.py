import numpy as np 

def function(x):

	p9 = x
	q2 = 9
	paths = []
	try:
		if q2 <= 2:
			p9 = 6/5
			x = 7-x
			q2 = q2*2
			paths.append(1)
		else:
			p9 = p9*1
			q2 = q2+7
			p9 = p9+p9
			paths.append(2)
		if x > 7:
			p9 = 6*0
			q2 = 9-6
			paths.append(3)
		else:
			x = x+7
			p9 = 5*p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))