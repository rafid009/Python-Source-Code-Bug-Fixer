import numpy as np 

def function(x):

	o0 = x
	m5 = 3
	paths = []
	try:
		if m5 < 3:
			m5 = o0-o0
			m5 = m5*2
			m5 = 8-3
			paths.append(1)
		else:
			x = x*5
			m5 = 5+m5
			m5 = m5*o0
			paths.append(2)
		if o0 < 7:
			o0 = o0+0
			x = 8+5
			x = 3*x
			paths.append(3)
		else:
			x = 2+7
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))