import numpy as np 

def function(x):

	u5 = 9
	q3 = x
	paths = []
	try:
		if u5 > 4:
			x = x+x
			x = 2+x
			u5 = 6-u5
			paths.append(1)
		else:
			u5 = 0+q3
			x = 7-0
			x = x-7
			paths.append(2)
		if x < 5:
			x = x-5
			u5 = u5*9
			x = x/8
			paths.append(3)
		else:
			q3 = q3/q3
			u5 = q3*0
			q3 = 0*3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))