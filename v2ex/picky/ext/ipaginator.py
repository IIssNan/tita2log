#!/usr/bin/python
# -*- coding=utf-8 -*-

'''
Created on Dec 29, 2009
@author: IIssNan
'''

from django.core.paginator import ObjectPaginator, InvalidPage

class Paginator(object):
  '''
  分页类 - 基于0.96版的Django paginator
  
  @param size: 分页所含条目数
  @param model: 待分页类型kind
  @param query: 查询条件字符串，如：WHERE name = 'cyndia'
  @param nu: 客户端提交的页码
  '''

  def __init__(self, size, entries, nu):
    '''
    @param size: 分页所含条目数
    @param model: 待分页类型kind
    @param nu: 客户端提交的页码
    
    @var number: 当前页码
    @var paginator: 分页器
    @var total: 总页数
    @var entries: 分页条目
    @var list: 页数列表
    '''
        
    self.number = self.get_number(nu)    
    self.paginator = ObjectPaginator(entries, size)
    self.total = self.paginator.pages
    self.entries = self.get_entries(int(self.number - 1), self.total)
    self.list = self.get_page_list(self.total)
  
  def get_number(self, nu):
    '''
    验证客户端提交页码
    @return: 页码x 或者 1
    '''
    
    try:
      return int(nu)
    except:
      return 1
    
  def is_paginator(self):
    '''
    是否可分页
    @return: True/False
    '''
    
    if self.total > 1:
      return True
    else:
      return False
  
  def get_entries(self, nu, total):
    '''
    获取内容
    @return: 内容
    '''
    
    try:
      entries = self.paginator.get_page(nu)
    except InvalidPage:
      entries = self.paginator.get_page(int(total - 1))
    
    return entries
                                        
  def has_previous_page(self):
    '''
    是否存在上一页
    @return: True/False
    '''
    
    if self.paginator.has_previous_page(self.number - 1):
      return True
    else:
      return False
  
  def has_next_page(self):
    '''
    是否存在下一页
    @return: True/False
    '''
    
    if self.paginator.has_next_page(self.number - 1):
      return True
    else:
      return False
    
  def get_page_list(self, total):
    '''
    获取页数列表
    @return: 列表'''
    
    if self.is_paginator():
      return [i for i in range(1, total + 1)]
