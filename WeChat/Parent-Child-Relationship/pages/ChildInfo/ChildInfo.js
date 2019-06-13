// pages/ChildInfo/ChildInfo.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    title: '孩子的热词',
  },
  
  dogTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Dog/Dog',
    })
  },

  cPositionTap: function () {
    wx.navigateTo({
      url: '/pages/Child/CPosition/CPosition',
    })
  },

  fishTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Fish/Fish',
    })
  },

  pigTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Pig/Pig',
    })
  },

  buddhaTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Buddha/Buddha',
    })
  },

  skrTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Skr/Skr',
    })
  },

  coldTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Cold/Cold',
    })
  },

  declareTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Declare/Declare',
    })
  },

  fragrantTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Fragrant/Fragrant',
    })
  },

  pigeonTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Pigeon/Pigeon',
    })
  },

  sourFishTap: function () {
    wx.navigateTo({
      url: '/pages/Child/SourFish/SourFish',
    })
  },

  lemonTap: function () {
    wx.navigateTo({
      url: '/pages/Child/Lemon/Lemon',
    })
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})